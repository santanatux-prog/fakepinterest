# Formulários usados no site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario
from flask_bcrypt import check_password_hash


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

    # def validate_email(self, email):
    #     # Verifica se o usuário existe
    #     usuario = Usuario.query.filter_by(email=email.data).first()
    #     if not usuario:
    #         raise ValidationError("Usuário inexistente ou senha inválida, crie uma conta")
    #     self.usuario = usuario  # guardamos o usuário para validar a senha depois
    #
    # def validate_senha(self, senha):
    #     # Só valida a senha se o usuário existir
    #     if hasattr(self, 'usuario'):
    #         if not check_password_hash(self.usuario.senha, senha.data):
    #             raise ValidationError("Senha incorreta")

    def validate(self, extra_validators=None):
        # Executa as validações básicas primeiro
        validacao_basica = super().validate(extra_validators=extra_validators)
        if not validacao_basica:
            return False

        usuario = Usuario.query.filter_by(email=self.email.data).first()

        # Verifica se o usuário existe e se a senha está correta
        if not usuario or not check_password_hash(usuario.senha, self.senha.data):
            self.email.errors.append("E-mail ou senha incorretos.")
            return False

        # Guarda o usuário validado para uso posterior
        self.usuario = usuario
        return True


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar")


class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")