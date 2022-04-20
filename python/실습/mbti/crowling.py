from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation


arguments = {"keywords":"""아이유, 민효린, 정려원, 뷔, RM, 전소민, 화사 ,진, 슈가, 정은지, 기안84
,제시,라미란, 이찬혁, 육성재
,태연, 카이, 태양, 김새론
,유주, 우기, 강다니엘, 찬열, 지민
,강동원, 서태지, 김유정, 손나은
,티파니, 키, 이특, 지코
,설현, 백현, 지효, 미나, 정국
,수영, 주이, 박봄, 백지영
,김연아, 쯔위, 소희, 크리스탈, 전지현
,재현, 정일훈, 레이나, 태현
,최강창민, 나르샤, 비니, 예지
,제이홉, 규현, 앤디, 혜리, 김신영
,성규, 써니, 차태현
,한채영, 김준수, 뱀뱀""" ,"limit":50,"print_urls":True, "format": "jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images