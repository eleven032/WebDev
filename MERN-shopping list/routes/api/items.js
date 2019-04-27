const express = require('express');
const router = express.Router();


//Item Model
const Item = require('../../models/Item');
//GET       api/items
//@desc     GET all items
//access    public
router.get('/',(req,res)=>{
    Item.find()
    .sort({data:-1})
    .then(items => res.json(items))
});

//POST       api/items
//@desc     Create a item
//access    public
router.post('/',(req,res)=>{
    const newItem = new Item({
        name: req.body.name
    });

    newItem.save().then(item=>res.json(item));

});


//DELETE       api/items
//@desc     delete a item
//access    public
router.delete('/:id',(req,res)=>{
    Item.findById(req.params.id)
        .then(item=>item.remove().then(()=>res.json({success:true})))
        .catch(err=>res.status(404).json({success:false}))

    

});

module.exports = router;