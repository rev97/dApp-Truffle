// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;
pragma experimental ABIEncoderV2;

contract ValidatorRatings {

    uint256 ValidationAccuracy;
    struct MlPeer {
        string name;
        uint256 m_rating;
    
    }
    struct SiteReviewer {
        string name;
        uint256 s_rating;
    
    }

    MlPeer[] public mlpeers; //array for list of mlpeers
    SiteReviewer[] public sitereviewers;
    mapping(string => uint256) public nameTomrating; //used to map name to ml peer rating, so you can get ml peer rating using name
    mapping(string => uint256) public nameTosrating; //used to map name to site plan reviewer rating, so you can get site plan reviewer rating using name

    function retrieve_ml() public view returns (MlPeer[] memory){
        return mlpeers; //retrieve tuple of all mlpeers
    }
    
    function retrieve_sr() public view returns (SiteReviewer[] memory){
        return sitereviewers; //retrieve tuple of all sitereviewers
    }

    function addmlpeer(string memory _name, uint256  _m_rating) public {
        mlpeers.push(MlPeer(_name, _m_rating)); //append to  MlPeer[] array
        nameTomrating[_name] = _m_rating; //use name to get ml peer rating
    }
    function addspreviwers(string memory _name, uint256 _s_rating) public {
        sitereviewers.push(SiteReviewer(_name, _s_rating)); //append to  SiteReviewer[] array
        nameTosrating[_name] = _s_rating; //use name to get site plan reviewer rating
    }
    
}