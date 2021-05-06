import $ from './includes/jquery';

import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    render() {
        return(<h1>Hello World!</h1>);
    }
}

export default App;

// Start React App
const e = $("#app").get(0);
if(e !== undefined)
    ReactDOM.render(<App/>, e);

// Remove page loader overlay
$(".page-loader-wrapper").delay(500).fadeTo('fast', 0, function(){
    $(this).remove();
});
