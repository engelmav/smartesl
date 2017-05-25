var React = require('react');
var MultipleChoice = require('./MultipleChoice');
var CreateMultipleChoice = require('./CreateMultipleChoice');

class App extends React.Component {
    render () {
        return (
            <div>
                <MultipleChoice />
                <CreateMultipleChoice />
            </div>
        )
    }
}

module.exports = App;