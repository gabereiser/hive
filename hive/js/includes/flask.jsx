import $ from 'jquery';

export const Flask = () => {
    return {
        flash_message: (parent_el, message) => {
            let flash = document.createElement('div');
            flash.className = 'flashes bg-danger';
            flash.style.display = 'none';
            flash.id = 'flash';
            let message_div = document.createElement('div');
            message_div.className = 'text-white';
            message_div.innerText = message;
            $(flash).append(message_div);
            $(parent_el).append(flash);
        }
    }
}
export default Flask;

export function flash_message (p, m){
    return Flask().flash_message(p, m);
}
