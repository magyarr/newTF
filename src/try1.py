import tensorflow as tf
import csv

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    
x_data=[]
y_data=[]
x_valid=[]
y_valid=[]
i=0
flen=file_len("EURUSD60.csv")
f = open('EURUSD60.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        i=i+1
        if (i<flen*0.1*8):
            x_data.append(float(row[2]))
            y_data.append(float(row[3]))
        else:
            x_valid.append(float(row[2]))
            y_valid.append(float(row[3]))
finally:
    f.close()

W = tf.Variable(tf.zeros([1,1]),name='W')
b = tf.Variable(tf.zeros([1]),name='b')
y = W * x_data + b

loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)


init = tf.initialize_all_variables()


sess = tf.Session()
sess.run(init)


for step in xrange(501):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))
# W=0.67433929,b=0.43560529
y1=[]
suc=0
for i in xrange(len(x_valid)):
    y1.append(0.67433929* x_valid[i]+0.43560529)
for i in xrange(len(x_valid)):
    if(y1[i]>x_valid[i] and y_valid[i]>x_valid[i]) :
        suc=suc+1
    if(y1[i]<x_valid[i] and y_valid[i]<x_valid[i]):
        suc=suc+1


print('Success {} % direction'.format(suc/float(len(x_valid))*100))
suc=0
for i in xrange(len(x_valid)):
    if(y1[i]==y_valid[i]) :
        suc=suc+1
print('Success {} % actual price'.format(suc/float(len(x_valid))*100))
       
        

    