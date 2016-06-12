import tensorflow as tf
import probabilityTester as dataSource
import numpy as np

x_data, y_data = dataSource.main()

W = tf.Variable(tf.zeros([60, 3]))
b = tf.Variable(tf.zeros([3]))
x = np.reshape(x_data,(10,60))
x = x.astype(np.float32,copy=False)
y = tf.nn.softmax(tf.matmul(x, W) + b)


loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)

test = raw_input("Enter Question Now:")

if len(test.split(" ")) < 20:
    for i in range(len(test.split(" ")), 20):
        test += " abcd"

ctxt = dataSource.findContext(test)
vect = []

for i in range(len(ctxt)):
    vect[3*i: 3*i + 2] = ctxt[i]

vect1 = np.reshape(vect, (1, 60))
vect1 = vect1.astype(np.float32, copy=False)
new = tf.matmul(vect1, sess.run(W)) + sess.run(b)
finalOut = sess.run(new)
print finalOut[0]
print max(max(finalOut))
maxiOut = 0;
maxiInd = 2;
for j in range(3):
    if(finalOut[0][j]> maxiOut):
        maxiOut = finalOut[0][j]
        maxiInd = j

if(maxiInd == 0):
    print "This Question Qualifies to the Payment Category. Confidence: %s" % (maxiOut/3)
else:
    print "Question Is not related to Payment Domain. Confidence: %s" % (maxiOut/3)
