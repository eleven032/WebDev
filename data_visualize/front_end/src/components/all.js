import React, { Component } from 'react';
import axios from 'axios';
import { Column, Table } from 'react-virtualized';
import 'react-virtualized/styles.css';


class DataList extends Component {

  constructor(props) {
    super(props);
    this.state = { datas: [] };
    
  }

  componentDidMount() {
    axios.get('http://localhost:4000/api')
      .then(response => {
        console.log(response);
        this.setState({ datas: response.data });
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  componentDidUpdate() {
    axios.get('http://localhost:4000/api')
      .then(response => {
        this.setState({ datas: response.data });
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  // dataList() {
  //     return this.state.datas.map(function(currentData, i) {
  //         return <Data data={currentData} key={i} />;
  //     });
  // }

  render() {
    return (
      <div>
        <h3>Keywords List</h3>
        {/* <table className="table table-striped" style={{ marginTop: 20 }}>
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
                </table> */}
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
    )
  }
}

export default DataList;