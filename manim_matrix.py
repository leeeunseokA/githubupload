from manim import *


class RotateVector(Scene):
    def construct(self):
        # 시작점과 벡터
        start_point = np.array([-3, -2, 0])
        vector = np.array([3, 2, 0])

        # 벡터 텍스트 라벨
        vector_label = MathTex("\\vec{v}").move_to(start_point + vector / 2)

        # 시작점과 끝점을 지정하여 화살표 생성
        arrow = Arrow(start_point, start_point + vector, buff=0)

        # 회전각
        angle = PI / 4

        # 회전 행렬 생성
        rotation_matrix = np.array([
            [np.cos(angle), -np.sin(angle)],
            [np.sin(angle), np.cos(angle)]
        ])

        # 3차원 벡터를 2차원으로 제한하여 회전
        rotated_vector_2d = np.dot(rotation_matrix, vector[:2])

        # 회전된 벡터를 다시 3차원으로 확장
        rotated_vector = np.array([rotated_vector_2d[0], rotated_vector_2d[1], 0])

        # 회전된 벡터 텍스트 라벨
        rotated_vector_label = MathTex("\\vec{v}'").move_to(start_point + rotated_vector / 2)

        # 회전된 벡터 생성
        rotated_arrow = Arrow(start_point, start_point + rotated_vector, buff=0, color=BLUE)

        # 애니메이션
        self.play(Create(arrow), Write(vector_label))
        self.wait(1)
        self.play(Transform(arrow, rotated_arrow), Transform(vector_label, rotated_vector_label))
        self.wait(1)