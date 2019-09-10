from PIL import Image
from PIL import ImageChops

#http://www.jianshu.com/p/5c2d63dea058

def compare_images(path_one, path_two, diff_save_location):
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)

    diff = ImageChops.difference(image_one, image_two)

    if diff.getbbox() is None:
        # 图片间没有任何不同则直接退出
        return
    else:
        diff.save(diff_save_location)

if __name__ == '__main__':
    # compare_images('11.jpg',
    #                '22.jpg',
    #                '44.jpg')
    compare_images('testpic/TEST3/1.jpg',
                   'testpic/TEST3/2.jpg',
                   '44.jpg')