import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def main():
    # Load our image
    # `mpimg.imread` will load .jpg as 0-255, so normalize back to 0-1
    img = mpimg.imread('test_images/warped_example.jpg') / 255

    # Create histogram of image binary activations
    histogram = hist(img)

    # Visualize the resulting histogram
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 18))
    f.tight_layout()
    ax1.imshow(img)
    ax1.set_title('Original Image', fontsize=50)
    ax2.plot(histogram)
    ax2.set_title('Histogram', fontsize=50)
    plt.subplots_adjust(left=0., right=1, top=1, bottom=0)
    plt.show()


def hist(img):
    # Grab only the bottom half of the image
    # Lane lines are likely to be mostly vertical nearest to the car
    bottom_half = img[img.shape[0] // 2:, :]

    # Sum across image pixels vertically - make sure to set an `axis`
    # i.e. the highest areas of vertical lines should be larger values
    histogram = np.sum(bottom_half, axis=0)

    return histogram


if __name__ == "__main__":
    main()
