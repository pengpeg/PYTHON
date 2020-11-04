import mxnet as mx

if __name__ == '__main__':
    x = mx.nd.ones((3, 4), ctx=mx.gpu())
    y = mx.nd.zeros((3, 4), ctx=mx.gpu())
    print(x)
    print('hello world!')
    