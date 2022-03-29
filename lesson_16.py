# Детектор людей на изображениях
# CLI:  python script.py Image_path

# pip install opencv-python


import argparse
import cv2

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(image):
    bb_box, weights = HOGCV.detectMultiScale(
        image,
        winStride=(4, 4),
        padding=(8, 8),
        scale=1.03
    )
    person = 1
    for x, y, w, h in bb_box:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )
        cv2.putText(
            image,
            f'Detecting {person}: {weights[person - 1]}',
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            1
        )
        person += 1
    # print(bb_box)
    # print(weights)
    return image, len(bb_box)


def main(args):
    image_path = args.image
    output_path = args.output
    img = cv2.imread(image_path)

    print(type(img))
    result_image, person_count = detect(img)
    cv2.imwrite(output_path, result_image)
    print(person_count)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('image', type=str, help='Image File path')
    parser.add_argument('--output', type=str, help='Output image path, (optional)')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    print(args)
    main(args)
