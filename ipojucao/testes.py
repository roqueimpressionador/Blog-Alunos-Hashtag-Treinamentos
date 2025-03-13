from main import app, database
from ipojucao.models import Usuario, Post
# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Lira", email='lira@gmail.com', senha="123456")
#     usuario2 = Usuario(username="João", email="joão@gmail.com", senha="123456")
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()
# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.posts)

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)

# with app.app_context():
#     database.creat_all()

# with app.app_context():
#     database.create_all()
#     Usuario.query.all()
#     meus_usuarios = Usuario.query.first()
#     print(meus_usuarios.username)
#     print(meus_usuarios.email)
#     print(meus_usuarios.senha)
