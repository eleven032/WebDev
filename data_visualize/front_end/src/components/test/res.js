// import React, { Component } from 'react'
// import { Column, Table } from 'react-virtualized';

// class Res extends Component {
//     constructor(props) {
//         super(props);
//         // console.log(props)
//         this.state = { datas: props.results };


//     }


//     render() {
//         return (
//             <div>
//                 <h3>Keywords List</h3>
//                 <Table
//                     width={800}
//                     height={800}
//                     headerHeight={20}
//                     rowHeight={30}
//                     rowCount={this.state.datas.length}
//                     rowGetter={({ index }) => this.state.datas[index]}
//                 >
//                     <Column
//                         label='Keywords'
//                         dataKey='keyword'
//                         width={200}
//                     />
//                     <Column
//                         width={200}
//                         label='Location'
//                         dataKey='location'
//                     />
//                     <Column
//                         width={200}
//                         label='Year'
//                         dataKey='year'
//                     />
//                     <Column
//                         width={200}
//                         label='Freq'
//                         dataKey='freq'
//                     />

//                 </Table>
//             </div>
//         )
//     }
// }


// export default Res;
import React from 'react';
import { Column, Table } from 'react-virtualized';


const Res = (props) => {

    return (
        <Table
            width={800}
            height={800}
            headerHeight={20}
            rowHeight={30}
            rowCount={props.results.length}
            rowGetter={({ index }) => props.results[index]}
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
    )

}

export default Res