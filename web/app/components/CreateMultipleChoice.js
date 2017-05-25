var React = require('react');
var PropTypes = require('prop-types');

class CreateMultipleChoice extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            questionBody: '',
            choices:[],
            answer: ''
        }
        this.setQuestionBody = this.setQuestionBody.bind(this);
    }

    setQuestionBody(event) {
        this.setState({ questionBody: event.target.value })
    }

    render () {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Question body:
                        <textarea
                            value={this.state.questionBody}
                            onChange={this.setQuestionBody} />
                    </label>
                </form>
            </div>
        )
    }
}

module.exports = CreateMultipleChoice;

{/*<h1>Multiple Choice Question Creator</h1>
<h2>Body</h2>
<form>
    <textarea type="text" placeholder="Enter question body here. Example: Twitter was _____ in 2006 by Jack Dorsey, Noah Glass, Biz Stone, and Evan Williams" />

    <h2>Choices</h2>

        <input type="text" placeholder="choice text" />
        <label class="checkbox-inline">
        <input type="checkbox">Correct answer</input>
        </label>
        <button>Remove</button>

    <button>Add Choice</button>

    <h2>What does this question test?</h2>

    <button>Add a Metatag</button>
    <input type="text" /></input>
    <button>Remove</button>

    <button>Save!</button>
</form>*/}