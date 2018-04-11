var React = require('react');
var PropTypes = require('prop-types');
var TagsInput = require('react-tagsinput');
var ReactTooltip = require('react-tooltip');
import axios from 'axios'
var smarteflApi = axios.create({ baseURL: 'http://localhost:5999/api/' });

class CreateMultipleChoice extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            questionBody: '',
            choices: ['choice 1', 'choice 2', 'choice 3'],
            tags: [],
            answer: ''
        }
        this.setQuestionBody = this.setQuestionBody.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleError = this.handleError.bind(this);
    }

    setQuestionBody(event) {
        this.setState({ questionBody: event.target.value })
    }

    handleChange (tags) {
        this.setState({ tags })
    }

    handleError (error) {
        console.log("Error attempting to save question:", error);
    }

    handleSubmit(e) {
        console.log('submitting question data')
        smarteflApi.post('/multi_choice/', this.state)
            .then((result) => console.log('posted'), (error) => { this.handleError(error) });
    }

    render() {
        var choiceInput = (choice, idx) => {
            return (
                <div key={idx}>
                    <input type="text" placeholder={choice} />
                    <input data-tip data-for="correctAnswer" type="checkbox"></input>
                    <ReactTooltip id="correctAnswer">
                        <span>Mark as correct answer</span>
                    </ReactTooltip>
                    <br />
                </div>
            )
        }
        return (
            <div>
                <h1>Multiple Choice Question Creator</h1>
                <p>The multiple choice question has a <a href="http://hackeducation.com/2015/01/27/multiple-choice-testing-machines">history</a>.</p>
                <form onSubmit={this.handleSubmit}>
                    <h2>Question Body</h2>
                    <p>Craft your question carefully. See the art of the multiple choice question.</p>
                    <textarea
                        placeholder='Enter question body here.'
                        value={this.state.questionBody}
                        onChange={this.setQuestionBody} />

                    <h2>Choices</h2>
                    <p>See guidelines and examples.</p>
                    {this.state.choices.map(choiceInput)}

                    <h2>Topics</h2>
                    <p>What language features does this question test?</p>
                    <TagsInput value={this.state.tags} onChange={this.handleChange} />
                    <br />

                    <button>Save Question</button>
                </form>
            </div>
        )
    }
}

module.exports = CreateMultipleChoice;