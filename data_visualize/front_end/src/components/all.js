import React, {Component} from 'react';
import axios from 'axios';
import {List} from "react-virtualized";

class Data extends Component {
  constructor(props) {
    super(props);
    console.log(props);
  }

  render() {
    return (
      <tr>
        <td>{this.props.data.keyword}</td>
        <td>{this.props.data.location}</td>
        <td>{this.props.data.year}</td>
        <td>{this.props.data.freq}</td>
      </tr>
    )}
}

class DataList extends Component {

    constructor(props) {
        super(props);
        this.state = {datas: []};
    }

    componentDidMount() {
        axios.get('http://localhost:4000/api')
            .then(response => {
              console.log(response);
              this.setState({datas: response.data});
            })
            .catch(function (error) {
              console.log(error);
            })
    }

    componentDidUpdate() {
        axios.get('http://localhost:4000/api')
        .then(response => {
          this.setState({datas: response.data});
        })
        .catch(function (error) {
          console.log(error);
        })   
    }

    dataList() {
        return this.state.datas.map(function(currentData, i) {
            return <Data data={currentData} key={i} />;
        });
    }

    render() {
        return (
            <div>
                <h3>Keywords List</h3>
                <table className="table table-striped" style={{ marginTop: 20 }}>
                    <thead>
                        <tr>
                            <th>Keyword</th>
                            <th>Location To</th>
                            <th>Year</th>
                            <th>Freq</th>
                        </tr>
                    </thead>
                    <tbody>
                        { this.dataList() }
                    </tbody>
                </table>
            </div>
        )
    }
}

export default DataList;