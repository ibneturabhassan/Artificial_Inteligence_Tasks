# This is implementation a multi-layer perceptron model (from scratch) to perform the logic Exclusive OR operation
# I have used 3 neurons. 2 in the hidden layer and 1 in output layer

THETA = 1

def neuron(input1, input2, weight1, weight2, theta):
    ans = (input1 * weight1) + (input2 * weight2)

    if ans < theta:
        output = 0
    else:
        output = 1

    return output

def hidden_layer(input1, input2, theta):
    a = neuron(input1, input2, 1.1, 1.1, theta)
    b = neuron(input1, input2, 0.6, 0.6, theta)
    return a, b

def xor_nn(input1, input2, theta):
    a, b = hidden_layer(input1, input2, theta)

    output_layer = neuron(a, b, 1.1, -2, theta)

    return output_layer


print('My XOR NN')

for p in range(0, 2):
    for q in range(0, 2):
        output = xor_nn(p, q, THETA)
        print('Input x: ' + str(p) + ', y: ' + str(q))
        print('Output: ' + str(output))
        print()
