>  # PyTorch로 한글 손글씨 인식하기
>
> 한국어를 표현하는 한글은 19개의 자음과 21개의 모음 문자를 가지고 있습니다. 이 문자들을 조합하면 최대 11,172개의 음절과 글자들을 표현할 수 있지만 그 중 일부만이 주로 사용됩니다. 이 프로젝트의 목표는 주로 사용되는 한글 손글씨를 인식 하는 신경망을 구축하는것 입니다.



> ## 데이터 생성
>
> 학습에 필요한 데이터는 폰트 파일을 사용하여 직접 생성하였습니다.

/fonts/ 디렉토리에는 데이터 생성에 사용되는 폰트 파일이 있습니다. 데이터 생성에는 아래의 8가지 폰트를 사용하였습니다.

![fonts.png](https://github.com/kusakina0608/Korean-Recognition/blob/master/img/fonts.png?raw=true)

/labels/ 디렉토리에는 자주 사용하는 한글 문자의 레이블이 나열되어 있는 txt 파일이 있습니다.

[korean-image-generator.ipynb](https://github.com/kusakina0608/Korean-Recognition/blob/master/tools/korean-image-generator.ipynb) 파일은 폰트 파일과 텍스트 파일을 사용하여 학습에 사용될 데이터를 생성합니다.



> ## 입력과 출력
>
> 

모델의 입력은 64x64 크기의 단일 한글 문자 이미지입니다. 이미지는 모델을 거쳐 입력으로 주어진 문자에 해당하는 UTF-8 코드를 출력합니다.