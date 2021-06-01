import tensorflow as tf


def main():
    logit_data = [2.0, 1.0, 0.2]
    output = tf.nn.softmax(logit_data)

    print(output)


if __name__ == "__main__":
    main()
