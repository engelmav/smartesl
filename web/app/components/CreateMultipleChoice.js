var React = require('react');
var PropTypes = require('prop-types');
var TagsInput = require('react-tagsinput');
require('react-tagsinput/react-tagsinput.css');

class CreateMultipleChoice extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            questionBody: '',
            choices:['choice1', 'choice2', 'choice3'],
            tags: [],
            answer: ''
        }
        this.setQuestionBody = this.setQuestionBody.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    setQuestionBody(event) {
        this.setState({ questionBody: event.target.value })
    }

    handleChange(tags){
        this.setState({tags})
    }

    render () {
        var choiceInput = (choice, idx) => {
            return ( 
                <div key={idx}>
                    <input type="text" placeholder={choice} />
                    <input type="checkbox"></input> 
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

                    <h2>Meta Tags</h2>
                    <p>Note what language features or vocabulary this question is testing. See our list of suggestions.</p>
                    <TagsInput value={this.state.tags} onChange={this.handleChange} />
                    <br />

                    <button>Save Question</button>
                </form>
            </div>
        )
    }
}

module.exports = CreateMultipleChoice;