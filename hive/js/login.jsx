

const Login = () => {
    return {
        loginHandler: (form) => {
            var data = {
                username: form.username.value,
                password: form.password.value,
                remember: form.remember.checked
            }
            $.post("/login", data, function(response) {
                if(response.status === 'ok')
                    window.location.href=response.redirect;
                else {
                    var flash = document.createElement('div');
                    flash.className = 'flashes bg-danger';
                    flash.style.display = 'none';
                    flash.id = 'flash';
                    for (var error of response.errors) {
                        var message = document.createElement('div');
                        message.className = 'text-white';
                        message.innerText = error;
                        $(flash).append(message);
                    }
                    $('.body').prepend(flash);
                    $(flash).fadeIn(250).delay(5000).fadeOut(250, function(){
                        $(this).remove();
                    });
                }
            });
            return false;
        }
    };
};
window.Login = Login;
export default Login;