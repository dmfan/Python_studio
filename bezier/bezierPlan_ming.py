#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Point:
    def __init__(self,xv=0.0,yv=0.0):
        self.x, self.y = xv, yv

def CubicBezier(t, controlPoint):   #　贝赛尔曲线　数学方程式
    p = Point()

    part0 = float(controlPoint[0].x * t ** 3)
    part1 = float(3.0 * controlPoint[1].x * t ** 2 * (1 - t))
    part2 = float(3.0 * controlPoint[2].x * t * (1 - t) ** 2)
    part3 = float(controlPoint[3].x * (1 - t) ** 3)
    p.x = part0 + part1 + part2 + part3

    part0 = float(controlPoint[0].y * t ** 3)
    part1 = float(3.0 * controlPoint[1].y * t ** 2 * (1 - t))
    part2 = float(3.0 * controlPoint[2].y * t * (1 - t) ** 2)
    part3 = float(controlPoint[3].y * (1 - t) ** 3)
    p.y = part0 + part1 + part2 + part3

    return p

class KeyFrame:
    def __init__(self,p=Point(),l=Point(),r=Point()):   # 动作目标点　　左控制点　　右控制点
        pLimit=Point()
        self.point = p
        self.leftCP = Point(self.point.x + l.x, self.point.y + l.y)
        self.rightCP = Point(self.point.x + r.x, self.point.y + r.y)

def toKeyFrames(frames):
    out = []
    for i in range(len(frames)):
        pointY=frames[i][0][1]
        pointX = frames[i][0][0]
        out.append(KeyFrame( Point(pointX, pointY), Point(frames[i][1][0], frames[i][1][1]), Point(frames[i][2][0], frames[i][2][1])))  # 得出　目标点　左右控制点
    return out

class BezierPlan:
    def __init__(self, dalta=10, frames=[], speedLimit=0.2, minData=-180, maxData=180):
        self.daltaX = dalta # ms
        self.frames = frames
        self.maxSpeed = speedLimit
        self.minValues=minData
        self.maxValues=maxData
        self.frameIdx = 0
        self.trajectory = []
        self.trajectoryLimit = []
        self.over = False

        self.control_redX = []  # point.x
        self.control_redY = []  # point.y
        self.control_bluX = []  # rightCP.x
        self.control_bluY = []  # rightCP.y
        self.control_greenX = []    # leftCP
        self.control_greenY = []    # leftCP

        self.originCurveX = []
        self.originCurveY = []

    def setFrames(self, frames):
        self.frames = frames

    def getTrajLen(self):
        return len(self.trajectory)

    def getTrajlimitLen(self):
        return len(self.trajectoryLimit)

    def valuesLimit(self,valueIn):
        if valueIn<self.minValues:
            valuesOut=self.minValues
        elif valueIn>self.maxValues:
            valuesOut=self.maxValues
        else:
            valuesOut=valueIn
        return valuesOut
        
    def planing(self):
        self.frameIdx = self.frameIdx + 1
        if(self.frameIdx==1):
            self.trajectoryLimit.append(self.frames[self.frameIdx-1].point)   # 添加第一个点
        if self.frameIdx >= len(self.frames):       # 全部点规划结束
            self.over = True
            return False

        controlPoint = []
        controlPoint.append(self.frames[self.frameIdx-1].point)
        controlPoint.append(self.frames[self.frameIdx-1].rightCP)
        controlPoint.append(self.frames[self.frameIdx].leftCP)
        controlPoint.append(self.frames[self.frameIdx].point)

        self.control_redX.append(self.frames[self.frameIdx-1].point.x)
        self.control_redY.append(self.frames[self.frameIdx-1].point.y)
        self.control_bluX.append(self.frames[self.frameIdx-1].rightCP.x)
        self.control_bluY.append(self.frames[self.frameIdx-1].rightCP.y)
        self.control_greenX.append(self.frames[self.frameIdx-1].leftCP.x)
        self.control_greenY.append(self.frames[self.frameIdx-1].leftCP.y)

        originCurve = []
        daltaT = float(self.daltaX) / (self.frames[self.frameIdx].point.x - self.frames[self.frameIdx-1].point.x)
        t = 1.0-daltaT
        while t>0:
            pp = CubicBezier(t,controlPoint)    # 根据数学公式离散化
            originCurve.append(pp)
            self.originCurveX.append(pp.x)#fftest
            self.originCurveY.append(pp.y)#fftest
            t = t-daltaT
        originCurve.append(self.frames[self.frameIdx].point)        # 添加最后一个点
        
        # 以上完成一段两帧间的曲线规划，将得到的离散化列表originCurve　在ｘ轴上统一时间间隔．１0ms
        time = self.frames[self.frameIdx-1].point.x + self.daltaX
        index = 1
        curveLimit = []
        curveLimit.append(Point(self.trajectoryLimit[-1].x, self.valuesLimit(self.trajectoryLimit[-1].y)))
        while time < self.frames[self.frameIdx].point.x:
            k = (originCurve[index].y-originCurve[index-1].y)/(originCurve[index].x-originCurve[index-1].x)
            kk = (originCurve[index].y-curveLimit[-1].y)/(originCurve[index].x-curveLimit[-1].x)
# ------------------------------------ 斜率 速度限制------------------------------------ #
            #maxSpeed
            if(time>=500):
                time=time
            if(abs(kk)>self.maxSpeed):
                if(kk>0):
                    pointY = curveLimit[-1].y + self.maxSpeed*(time - curveLimit[-1].x)
                else:
                    pointY = curveLimit[-1].y - self.maxSpeed*(time - curveLimit[-1].x)
            else:
                pointY = curveLimit[-1].y + kk*(time - curveLimit[-1].x)
            curveLimit.append(Point(time, self.valuesLimit(pointY)))
# ------------------------------------ 斜率 速度限制------------------------------------ #
            self.trajectory.append(Point(time, originCurve[index-1].y+k*(time-originCurve[index-1].x)))
            # print("time:",time,"x:",originCurve[index].x)#fftest
            # print("origin y:",originCurve[index-1].y,"y:",originCurve[index-1].y+k*(time-originCurve[index-1].x))#fftest

            time = time + self.daltaX
            while time > originCurve[index].x:
                index = index + 1
            
        self.trajectory.append(self.frames[self.frameIdx].point)        # 添加最后一个点

        # curveLimit添加最后一个点
        k = (self.frames[self.frameIdx].point.y-curveLimit[-1].y)/(self.frames[self.frameIdx].point.x-curveLimit[-1].x)
        if(abs(k)>self.maxSpeed):
            if(k>0):
                pointY = curveLimit[-1].y + self.maxSpeed*(time - curveLimit[-1].x)
            else:
                pointY = curveLimit[-1].y - self.maxSpeed*(time - curveLimit[-1].x)
        else:
            pointY = curveLimit[-1].y + k*(time - curveLimit[-1].x)
        curveLimit.append(Point(self.frames[self.frameIdx].point.x, self.valuesLimit(pointY)))
        curveLimit.pop(0)
        self.trajectoryLimit.extend(curveLimit)
        
        return True

    def getTrajectory(self, length):
        if length <= len(self.trajectory):
            out = self.trajectory[:length]
            del self.trajectory[:length]        #! ffflag
            return out
        raise Exception("input length out of range!")

    def getTrajectoryLimit(self, length):
        if length <= len(self.trajectoryLimit):
            out = self.trajectoryLimit[:length]
            del self.trajectoryLimit[:length]    #! ffflag
            return out
        raise Exception("input length out of range!")


class MultiBeizerPlan:
    def __init__(self,number, dalta, frames, speedLimits, speedLimit=0.2):
        self.numberOfTraj = number
        self.bPlanObj = []
        for i in range(self.numberOfTraj):
            self.bPlanObj.append(BezierPlan(dalta, toKeyFrames(frames[i]), speedLimit, speedLimits[i][0], speedLimits[i][1]))

    def planing(self, length):
        for i in range(self.numberOfTraj):
            if self.bPlanObj[i].over == False:
                while self.bPlanObj[i].getTrajLen() <= length:
                    if self.bPlanObj[i].planing() == False:
                        break
    
    def getTrajectory(self, length):
        traj = []
        for i in range(self.numberOfTraj):
            if self.bPlanObj[i].over == False:
                temp = self.bPlanObj[i].getTrajectory(length)
                if temp:
                    traj.append(temp)
            else:
                temp = self.bPlanObj[i].getTrajectory(self.bPlanObj[i].getTrajLen())
                if temp:
                    traj.append(temp)

        return traj

    def sendComplete(self):
        number = 0
        for i in range(self.numberOfTraj):
            if self.bPlanObj[i].getTrajLen() == 0:
                number += 1
        if number == self.numberOfTraj:
            return True
        return False


# example
if __name__ == '__main__':
    from matplotlib import pyplot as plt 

    angleLimitSet = [
        [-70,170]
    ]
    speedLimitSet = 3
    frames = [
        #[x,   y]
        # [[500, -50], [-100, 0], [100, 0]],
        # [[1100, 0], [-100, 0], [100, 0]],
        # [[1400, 50], [-100, 0], [100, 0]],
        # [[2000, -50], [-100, 0], [100, 0]],
        # [[2400, -80], [-100, 0], [100, 0]],
        # [[3000, 70], [-100, 0], [100, 0]],
        # [[3400, 30], [-100, 0], [100, 0]],


        [[0, 0], [0, 0], [30, 0]],
        [[100, 100], [-30, 0], [30, 0]],
        [[200, 0], [-30, 0], [0, 0]],
    ]
    # frames.insert(0, [[0, -50], [0, 0], [100, 0]])

    bPlan = BezierPlan(10, toKeyFrames(frames),speedLimitSet,angleLimitSet[0][0],angleLimitSet[0][1])

    plotX = []
    plotY = []

    plotXlimit = []
    plotYlimit = []

    while True:
        while bPlan.getTrajLen() <= 12:
            if bPlan.planing() == False:    # 全部点规划结束
                break

        if bPlan.over == True:
            break
        
        trajectory = bPlan.getTrajectory(4)
        for i in range(len(trajectory)):
            plotX.append(trajectory[i].x)
            plotY.append(trajectory[i].y)

        trajectoryLimit = bPlan.getTrajectoryLimit(4)
        for i in range(len(trajectoryLimit)):
            plotXlimit.append(trajectoryLimit[i].x)
            plotYlimit.append(trajectoryLimit[i].y)

    trajectory = bPlan.getTrajectory(bPlan.getTrajLen())
    for i in range(len(trajectory)):
        plotX.append(trajectory[i].x)
        plotY.append(trajectory[i].y)

    trajectoryLimit = bPlan.getTrajectoryLimit(bPlan.getTrajlimitLen())
    for i in range(len(trajectoryLimit)):
        plotXlimit.append(trajectoryLimit[i].x)
        plotYlimit.append(trajectoryLimit[i].y)

    plt.scatter(plotX, plotY, marker='.',c='r')
    plt.scatter(plotXlimit, plotYlimit, marker='v',c='y')
    plt.scatter(bPlan.control_redX,bPlan.control_redY,c='r')
    plt.scatter(bPlan.control_bluX,bPlan.control_bluY,c='b')
    plt.scatter(bPlan.control_greenX,bPlan.control_greenY,c='g')
    # plt.scatter(bPlan.originCurveX,bPlan.originCurveY,c='y')
    
    plt.show()
