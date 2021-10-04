import React from "react";
import {Checkbox, TableCell, TableRow, Typography} from "@material-ui/core";



export default class Tablerow extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            checked: this.props.checked,
            name: this.props.name
        };
    }

    render() {

        return (
            <div>
                <TableRow
                    key={this.props.name}
                    sx={{"&:last-child td, &:last-child th": {border: 1}}}
                >
                    <TableCell padding="checkbox">
                        <Checkbox
                            color="primary"
                            checked={this.props.checked}
                            onChange={() => this.props.checkFunction(this.props.id)}
                            inputProps={{
                                "aria-label": "select all desserts"
                            }}
                        />
                    </TableCell>
                    <TableCell component="th" scope="row" size="medium" sx={{weight:100}}>
                        <Typography  >{this.props.name} </Typography>
                    </TableCell>
                </TableRow>
            </div>
        );
    }
}
