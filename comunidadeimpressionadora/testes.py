from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post

with app.app_context():
    # database.drop_all()
    # database.create_all()
    # usuario = Usuario(username='Lira', email='lira@gmail.com', senha='123456')
    # usuario2 = Usuario(username='João', email='joao@gmail.com', senha='123456')
    # database.session.add(usuario)
    # database.session.add(usuario2)
    # database.session.commit()

    meus_usuarios = Usuario.query.all()
    print(meus_usuarios)
    # primeiro_usuario = meus_usuarios[0]
    primeiro_usuario = Usuario.query.first()
    print(primeiro_usuario.id)
    print(primeiro_usuario.email)
    print(primeiro_usuario.cursos)
    # usuario_teste = Usuario.query.filter_by(email='lira@gmail.com').first()
    # print(usuario_teste.id)
    # print(usuario_teste.username)
    # print(usuario_teste.posts)

    # meu_post = Post(id_usuario=1, titulo='Primeiro Post do Lira', corpo='Lira voando')
    # database.session.add(meu_post)
    # database.session.commit()

    # post_teste = Post.query.first()
    # print(post_teste.titulo)
    # print(post_teste.autor.email)