import React, { Component } from 'react';
import axios from 'axios';
import { Column, Table } from 'react-virtualized';
import 'react-virtualized/styles.css';


class Search extends Component {
    constructor(props) {
        super(props);
        this.state = {
            keyword: "",
            datas: []
        };
        this.handleSearchTextUpdate = this.handleSearchTextUpdate.bind(this);
    }


    componentDidMount() {
        this.setState({
            keyword: this.props.word
        });
        axios.get('http://localhost:4000/api/:' + this.state.keyword)
            .then(response => {
                console.log(response);
                this.setState({ datas: response.data });
            })
            .catch(function (error) {
                console.log(error);
            })
    }

    componentWillReceiveProps(nextProps) {
        this.setState({
            keyword: nextProps.word
        });
        axios.get('http://localhost:4000/api/:' + this.state.keyword)
            .then(response => {
                console.log(response);
                this.setState({ datas: response.data });
            })
            .catch(function (error) {
                console.log(error);
            })
    }


    handleSearchTextUpdate (searchText) {
        
        this.setState({keyword:searchText});
      };

    render() {
        return (
            <div className="searchBox">
                <input type="text" placeholder="type in keywords to search" onSearchTextUpdate={this.handleSearchTextUpdate}/>
                <Table
                    width={800}
                    height={800}
                    headerHeight={20}
                    rowHeight={30}
                    rowCount={this.state.datas.length}
                    rowGetter={({ index }) => this.state.datas[index]}
                >
                    <Column
                        label='Keywords'
                        dataKey='keyword'
                        width={200}
                    />
                    <Column
                        width={200}
                        label='Location'
                        dataKey='location'
                    />
                    <Column
                        width={200}
                        label='Year'
                        dataKey='year'
                    />
                    <Column
                        width={200}
                        label='Freq'
                        dataKey='freq'
                    />

                </Table>
            </div>

        );
    }
}
export default Search;