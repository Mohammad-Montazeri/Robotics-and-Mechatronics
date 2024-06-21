# samples and initial parameters
inputs = [(1, -1), (0, 2), (2, 1)]  # (x1_i , x2_i)
outputs = [-1, -1, 1]   # y1, y2, y3
weights = [-1, 1, 0.5]  # w0, w1, w2
alpha = 0.5

# learning algorithm
for i in range(100):    # epochs loop
    error = 0
    print(f'--- epoch {i+1} ---')
    for x, y in zip(inputs, outputs):   # samples loop
        z = 1 * weights[0] + x[0] * weights[1] + x[1] * weights[2]
        if z >= 0:
            yp = 1
        else:
            yp = -1
        err = y - yp
        error += abs(err)

        if err:
            weights[0] += alpha * err
            weights[1] += alpha * err * x[0]
            weights[2] += alpha * err * x[1]

    print('w0, w1, w2 =', weights)
    print('total error =', error)
    if not error:
        break

# test
'''
# test to see if the result really satisfies the samples (should be test data we lack...)
# for i, x in enumerate(inputs):
#     z = 1 * weights[0] + x[0] * weights[1] + x[1] * weights[2]
#     if z >= 0:
#         yp = 1
#     else:
#         yp = -1
#     y = outputs[i]
#     err = yp - y
#     print(f'error of sample-{i+1} = {err}')
'''