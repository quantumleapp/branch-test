import os
import face_recognition

# images 폴더 안의 사진으로 list 생성 (출석체크 대기자)
student_images = os.listdir('images')
print(student_images) # test code (image)
print()

# {student_name : 출석여부} 의 dictionary 생성 (출석부)
student_dic = {}
for student in student_images:
    
        if student.count(".") == 1: 
            name = student.split('.')[0]
            student_dic[name] = '결석'

# student_dic 출력
def name_print():
    for name, val in student_dic.items():
        print(name, val)

    print('\n-------------------------\n')
    main()

# 출석체크 (얼굴 인식 등 출석체크 상황을 이미지 업로드로 대체)
def attendance():
    # 인식할 얼굴 (출석체크한 학생)
    student_name = input('파일을 업로드 하세요(ex: name.jpg) : ')
    print()

    # 업로드한 이미지에서 얼굴 인식
    image_to_recognition = face_recognition.load_image_file(student_name)
    image_to_recognition_encoded = face_recognition.face_encodings(image_to_recognition)[0]

    # 위에서 만든 리스트 student_images (출석체크 대기자) / 얼굴 인식 -> 업로드한 이미지(출석체크한 학생)와 비교
    for student_image in student_images:

        # 출석체크 대기자 얼굴 인식
        student = face_recognition.load_image_file('images/' + student_image)
        student_encoded = face_recognition.face_encodings(student)[0]

        # 출석체크 대기자 얼굴과 출석체크한 학생의 얼굴을 비교
        result = face_recognition.compare_faces([image_to_recognition_encoded], student_encoded)

        # 파일명에서 확장자 제거
        if student_image.count(".") == 1: 
            name = student_image.split('.')[0]

        # 일치 여부에 따른 student_dic 수정, 해당 key, value 출력
        if result[0] == True:
            student_dic.update({name:'[출석]'})
            print(name, student_dic[name])
        else:
            print(name, student_dic[name])
    print('\n-------------------------\n')
    main()

# 출석체크 시스템 실행
def main():
    print('출석체크 시스템입니다\n')
    print('1. 명단 확인\n2. 출석체크\n3. 종료\n')
    func = int(input('실행할 기능의 번호를 입력하세요 : '))
    print()

    if func == 1:
        name_print()
    elif func == 2:
        attendance()
    elif func == 3:
        print('종료합니다\n')
    else:
        print('Error..\n')
        main()

# main
main()