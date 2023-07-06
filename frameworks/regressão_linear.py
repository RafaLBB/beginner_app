# Modelo de regressão linear com Tensorflow
# Aula: DSA

#Certifique-se que a versão do tensorflow utilizada seja a mesma que utilizarei neste exmplo, pra isso
 
!pip install -q tensorflow==1.15.2

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Hyperparâmetros do modelo
# Alguns parâmetros do modelo devem ser ajustados manualmente, como por exemplo: 

learning_rate = 0.01
training_epochs = 2000
display_step = 200

# Para criarmos um modelo, precisamos ensinar com dados históricos, para que possa se basear quando efetuar alguma predição.
# Os datasets de testes devem ser diferentes dos de treinamento, para que o resultado do teste não se torne enviesado.

# Dataset de treino
train_x = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_y = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]
 
# Dataset de teste
test_x = np.asarray([6.83, 4.668, 8.9, 7.91, 5.7, 8.7, 3.1, 2.1])
test_y = np.asarray([1.84, 2.273, 3.2, 2.831, 2.92, 3.24, 1.35, 1.03])


# Agora precisamos definir os Placeholders e variáveis.
# Em outras palavras os tensores que serão alimentados durante o treinamento junto com seus pesos e bias.

# Placeholders para as variáveis preditoras (x) e para  variável target (y)
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
 
# Pesos e bias do modelo
w = tf.Variable(np.random.randn(), name="weight")
b = tf.Variable(np.random.randn(), name="bias")

# Precisamos construir o modelo linear 
# Fórmula do modelo linear: y = W*X + b
linear_model = w*x + b
# Comparando o erro com o dado real ( y ), pois assim o peso será realimentado com um dado mais preciso.
cost = tf.reduce_sum(tf.square(linear_model - y)) / (2*n_samples)
 
# Calcula a derivada a partir do erro, volta com o backpropagation e atualiza os pesos.
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)


# Até agora nenhum modelo foi ensinado. Pra que isso aconteça, no tensorflow precisamos abrir uma sessão e assim executar o grafo computacional.

# Definindo a inicialização das variáveis
init = tf.global_variables_initializer()
 
# Iniciando a sessão
with tf.Session() as sess:
    # Iniciando as variáveis
    sess.run(init)
 
    # Treinamento do modelo
    #lembrando que o "training_epochs" já foi definido lá em cima.
    for epoch in range(training_epochs):
 
        # Otimização com Gradient Descent
        # feed_dict alimenta os tensores x e y com os valores historicos
        sess.run(optimizer, feed_dict={x: train_x, y: train_y})
         
        # Display de cada epoch
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={x: train_x, y: train_y})
            print("Epoch:{0:6} \t Custo (Erro):{1:10.4} \t W:{2:6.4} \t b:{3:6.4}".format(epoch+1, c, sess.run(W), sess.run(b)))
             
    # Imprimindo os parâmetros finais do modelo
    print("\nOtimização Concluída!")
    training_cost = sess.run(cost, feed_dict={x: train_x, y: train_y})
    print("Custo Final de Treinamento:", training_cost, " - W Final:", sess.run(W), " - b Final:", sess.run(b), '\n')
     
    # Visualizando o resultado
    plt.plot(train_x, train_y, 'ro', label='Dados Originais')
    plt.plot(train_x, sess.run(W) * train_x + sess.run(b), label='Linha de Regressão')
    plt.legend()
    plt.show()
 
    # Testando o modelo
    testing_cost = sess.run(tf.reduce_sum(tf.square(linear_model - y)) / (2 * test_x.shape[0]), 
                            feed_dict={x: test_x, y: test_y})
     
    print("Custo Final em Teste:", testing_cost)
    print("Diferença Média Quadrada Absoluta:", abs(training_cost - testing_cost))
 
    # Display em Teste
    plt.plot(test_x, test_y, 'bo', label='Dados de Teste')
    plt.plot(train_x, sess.run(x) * train_X + sess.run(b), label='Linha de Regressão')
    plt.legend()
    plt.show()
    
sess.close()
