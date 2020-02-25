from unittest import TestCase
import pure_pursuit as m

print("pure_pursuit test")



class Test(TestCase):

    def test1(self):
        m.show_animation = False
        m.main()

    def test2(self):
        cx = [0,1,2,3]  #needs at least three points, and at least one outside the look-ahead distance
        cy = [0,0,0,0]
        testPath = m.Trajectory(cx,cy)
        #start at origin, not moving
        state = m.State(x=-0.0, y=0, yaw=0.0, v=0.0)
        #could check initialIndex was correct if look-ahead distance (Lfc) was accessible
        initialIndex = testPath.search_target_index(state)

        #asking again shouldn't change the answer:
        iteratedIndex = testPath.search_target_index(state)
        iteratedIndex = testPath.search_target_index(state)
        if (initialIndex != iteratedIndex):
            raise Exception("incorrect index returned by Trajectory.search_target_index")

Thistest = Test()
Thistest.test1()
Thistest.test2()
print("done")
