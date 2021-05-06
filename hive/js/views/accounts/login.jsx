import $ from '../../includes/jquery'
import flash_message from '../../includes/flask'

const Login = () => {
    return {
        loginHandler: (form) => {
            const data = {
                username: form.username.value,
                password: form.password.value,
                remember: form.remember.checked
            }
            $.post("/api/auth/login", data, function(response) {
                if(response.status === 'ok') {
                    if (response.redirect == null) {
                        response.redirect = '/';
                    }
                    window.location.href = response.redirect;
                }
                else {
                    flash_message($('.body'), response.error);
                }
            });
            return false;
        }
    };
};
window.Login = Login;
export default Login;