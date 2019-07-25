import React, { Component } from 'react';
import axios from 'axios';
import Res from './test/res';

class Search extends Component {
    constructor(props) {
        super(props);
        this.state = {
            keyword: "",
            datas: []
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        // this.getInfo = this.getInfo.bind(this);
    }

    // getInfo = () => {

    // }

    handleInputChange = () => {
        this.setState({
            keyword: this.search.value
        })
    }

    handleSubmit(event) {
        // this.getInfo();
        axios.get(`http://localhost:4000/api/${this.state.keyword}`)
            .then(res => {
                this.setState({
                    datas: res.data
                })
                // console.log(res.data)
                // console.log(this.state.datas)
            })
            // console.log(this.state.datas)
        event.preventDefault();

    }


    render() {
        // console.log(this.state.datas)
        return (
            <form onSubmit={this.handleSubmit}>
                <input
                    placeholder="Search for..."
                    ref={input => this.search = input}
                    onChange={this.handleInputChange}
                />
                <input type="submit" value="Submit" />
                <Res results={this.state.datas} />

            </form>


        );
    }
}
export default Search;