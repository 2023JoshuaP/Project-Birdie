import { Avatar } from "@mui/material";
import React from "react";
import { Link } from "react-router-dom";
import useUserContext from "../../contexts/UserContext";
import PropTypes from "prop-types";  // Correcta importación

const UserProfileCard = (props) => {
    const { id, profile_pic, username, followers } = props;
    const {
        profileData: { id: userId },
    } = useUserContext();

    return (
        <div className="mt-2 pl-3 p-2 bg-gray-50 w-full flex gap-2 items-center rounded-lg dark:bg-[#030108]">
            <Avatar src={profile_pic || null} alt={username}>
                {username.at(0).toUpperCase()}
            </Avatar>
            <div className="flex flex-col mr-auto">
                <div className="text-sm dark:text-gray-100">{id === userId ? "You" : username}</div>
                <div className="text-[.75rem] text-gray-600">
                    {followers === 1 ? "1 follower" : followers + " followers"}
                </div>
            </div>
            <Link
                to={id === userId ? "/profile" : `/user/${id}/`}
                className="float-right m-4 border-2 hover:bg-purple-500 hover:border-purple-100 hover:text-purple-100 p-1 px-2 rounded-full text-purple-500 text-[.7rem] border-purple-500"
            >
                View Profile
            </Link>
        </div>
    );
};

// Validación de las props usando PropTypes
UserProfileCard.propTypes = {
    id: PropTypes.string.isRequired,        // 'id' debe ser un string y es requerido
    profile_pic: PropTypes.string,          // 'profile_pic' debe ser un string, pero es opcional
    username: PropTypes.string.isRequired,  // 'username' debe ser un string y es requerido
    followers: PropTypes.number.isRequired, // 'followers' debe ser un número y es requerido
};

export default UserProfileCard;
