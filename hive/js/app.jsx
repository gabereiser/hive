import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    render() {
        return(<h1>Hello World!</h1>);
    }
};

export default App;

// Start React App
const e = $("#app").get(0);
if(e !== undefined)
    ReactDOM.render(<App/>, e);


// Remove page loader overlay

$(".page-loader-wrapper").delay(1000).fadeTo('slow', 0, function(){
    $(this).remove();
});

