import * as React from 'react';
import {Table, TableContainer, Paper, TableBody, Button} from '@material-ui/core';
import Tablerow from '../components/table'
import ModalEdit from '../components/modal_edit'
import ModalNew from '../components/modal_new'
import Stack from '@mui/material/Stack';
import {apiTaskAll, apiTaskDelete, apiTaskAdd, apiTaskRename, apiTaskCheck} from "../api/api";


export default class Todolist extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            data: []

        };
    }

    componentDidMount() {
        apiTaskAll().then(response => {
            try {
                const data1 = response.data;
                this.setState({data: data1})

            } catch (err) {
                console.log('eeeeror')
            }
        });
    }


    handleChange = (id, name, checked) => {
        let data1 = this.state.data;
        const index = data1.findIndex(x => x.id === id)
        data1[index].name = name;
        this.setState({data: data1});
        apiTaskRename(id, name, checked)
    };

    checkFunction = (id) => {
        let data1 = this.state.data;
        const index = data1.findIndex(x => x.id === id)
        data1[index].checked = !data1[index].checked;
        this.setState({data: data1});
        apiTaskCheck(id,data1[index].checked)

    };

    handldelete = (id) => {
        let data1 = this.state.data;
        data1 = data1.filter(data1 => data1.id !== id)
        this.setState({data: data1});
        apiTaskDelete(id)
    }
    handladd = (name) => {
        apiTaskAdd(name, false)
        this.componentDidMount()
    }





    render() {
        return (
            <div >
                <h1 style={{marginLeft: 540}}>My TODO list</h1>
                <TableContainer component={Paper}>
                    <Table sx={{minWidth: 850}} size="norm" aria-label="a dense table">
                        <TableBody>
                            {this.state.data.map((row) => (
                                <Stack direction="row" spacing={3} >
                                    <Tablerow
                                        checkFunction={this.checkFunction}
                                        name={row.name}
                                        checked={row.checked}
                                        id={row.id}
                                    />
                                    <ModalEdit
                                        handleChange={this.handleChange}
                                        id={row.id}
                                        checked={row.checked}

                                    />
                                    <Button
                                        variant="contained"
                                        style = {{marginLeft:"auto"}}
                                        onClick={() => {
                                            this.handldelete(row.id);
                                        }}
                                    >
                                        Удалить
                                    </Button>
                                </Stack>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
                <ModalNew

                    handleChange={this.handladd}
                />
            </div>
        );
    }
};