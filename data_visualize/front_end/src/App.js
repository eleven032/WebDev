import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  state = {
    infos:[]
  }


  render(){
    const {infos} = this.state;
    return (
      <div className="App">
        {infos.map(this.renderInfo)}
      </div>
    );
  }
  

export default App;
