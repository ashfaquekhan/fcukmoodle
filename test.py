

while True:

    raw_input('Press ENTER to start searching text')
    OCR_time = time.time()

    box_names = ['question', 'choice1', 'choice2', 'choice3']
    images = [box.sub_boxes[box_name].get_image() for box_name in box_names]

    print(images)

    texts = []


    print(texts)

    # print 'question', box.get_sub_box_text('question')
    # print 'choix1', box.get_sub_box_text('choice1')
    # print 'choix2', box.get_sub_box_text('choice2')
    # print 'choix3', box.get_sub_box_text('choice3')


    print('OCR time'), time.time() - OCR_time