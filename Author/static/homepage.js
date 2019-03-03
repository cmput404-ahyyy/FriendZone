'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }
    const content = 'test';
    return (
      e(
        'button',
        { onClick: () => this.setState({ liked: true }) },
        'Like'
      ) 
      // <div className='234'>
      //   <h1>hello</h1>
      // </div>
    );
      
  }
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);