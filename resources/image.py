from flask_restful import Resource
from flask_uploads import UploadNotAllowed
from flask import request, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
import traceback
import os
from libs import image_helper



class ImageUpload(Resource):
    @classmethod
    def post(cls):
        """
        Upload image file
        """
        data = request.files
        # FileStorage obj
        # 
        user_id = get_jwt_identity()
        folder = f"user_{user_id}" # static/images/user_1
        try:
            image_path = image_helper.save_image(data['image'], folder=folder)
            basename = image_helper.get_image_basename(image_path)
            return {'message': f"File: {basename} Uploaded"}, 201
        except UploadNotAllowed:
            extension = image_helper.get_extension(data['image'])
            return {"message": f"{extension} not allowed"}, 400


class Image(Resource):
    @classmethod
    def get(cls, filename: str):
        """
        Return requested image for user if exists
        """
        user_id = get_jwt_identity()
        folder = f"user_{user_id}"
        if not image_helper.is_filename_safe():
            return {"message": f"Image illegal filename"}, 400
        try:
            return send_file(image_helper.get_path(filename, folder=folder)), 200
        except FileNotFoundError:
            return {'message': 'Image not found'}, 404


    @classmethod
    def delete(cls, filename: str):
        """
        Allow an user to delete an image 
        """
        user_id = get_jwt_identity()
        folder = f"user_{user_id}"
        if not image_helper.is_filename_safe():
            return {"message": f"Image illegal filename"}, 400
        try: 
            os.remove(image_helper.get_path(filename, folder=folder))
            return {"message": "Image Deleted"}, 200
        except FileNotFoundError:
            return {"message": "Image not found"}, 404
        except:
            traceback.print_exc()
            return {"message": " Failed to delete image"}, 500


class AvatarUpload(Resource):
    @classmethod
    def put(cls):
        """
        Upload user avatar.
        Users have unique avatar.
        """
        data = request.files
        filename = f"user_{get_jwt_identity()}"
        folder = "avatars"
        avatar_path = image_helper.find_image_any_format(filename, folder)
        if avatar_path:
            try:
                os.remove(avatar_path)
            except:
                return {"message": "Failed to delete avatar"}, 500

        try:
            ext = image_helper.get_extension(["image"].filename)
            avatar = filename + ext
            avatar_path = image_helper.save_image(
                data["image"],
                folder=folder,
                name=avatar
            )

            basename = image_helper.get_image_basename(avatar_path)
            return {"message": f"Uploaded {basename}"}, 200
        except UploadNotAllowed:
            extension = image_helper.get_extension(data["image"])
            return {"message": f"Extension {extension} not allowed"}, 400


class Avatar(Resource):
    @classmethod
    def get(cls, user_id: int):
        folder = 'avatars'
        filename = f"user_{user_id}"
        avatar = image_helper.find_image_any_format(filename)
        if avatar:
            return send_file(avatar)
        return {"message": "Avatar not found"}, 404
