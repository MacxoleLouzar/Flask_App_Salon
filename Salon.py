from bson import ObjectId
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from DB import mongo
from werkzeug.utils import secure_filename
import os



salon_blueprint = Blueprint('salon', __name__)

@salon_blueprint.route('/create_salon', methods=['GET', 'POST'])
def create_salon():
    if request.method == 'POST':
        owner_name = request.form['owner_name']
        salon_name = request.form['salon_name']
        salon_logo = request.files['salon_logo']  # Get the uploaded salon logo file
        address = request.form['address']
        phone_number = request.form['phone_number']
        salon_description = request.form['salon_description']

        # Check if salon with the same name and address already exists
        existing_salon = mongo.db.salons.find_one({'salon_name': salon_name, 'address': address})
        if existing_salon:
            flash('Salon with the same name and address already exists.', 'error')
            return redirect(url_for('salon.create_salon'))
        
        # Save the uploaded salon logo file to the server
        if 'salon_logo' in request.files:
            salon_logo = request.files['salon_logo']
            if salon_logo.filename != '':
                filename = secure_filename(salon_logo.filename)
                salon_logo.save(os.path.join(current_app.config['UPLOAD_FOLDER'] ,filename))

      # Save the salon data to MongoDB
        mongo.db.salons.insert_one({
            'owner_name': owner_name,
            'salon_name': salon_name,
            'salon_logo_filename': filename,
            'address': address,
            'phone_number': phone_number,
            'salon_description': salon_description
        })
        # Redirect to a success page or another route
        flash('Salon created successfully!', 'success')
        return redirect(url_for('salon.salon_view'))

    return render_template('Salon/CreateSalon.html')

@salon_blueprint.route('/create_salon_success')
def create_salon_success():
    return 'Salon created successfully!'

#View List of Salons
@salon_blueprint.route('/salon_view')
def salon_view():
    salons = mongo.db.salons.find()
    return render_template('Salon/SalonViewList.html', salons=salons)

#Edit Salon

@salon_blueprint.route('/edit_salon/<string:id>', methods=['GET', 'POST'])
def edit_salon(id):
    salon = mongo.db.salons.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        owner_name = request.form['owner_name']
        salon_name = request.form['salon_name']
        salon_logo = request.files['salon_logo']
        address = request.form['address']
        phone_number = request.form['phone_number']
        salon_description = request.form['salon_description']
        
        if 'salon_logo' in request.files:
            salon_logo = request.files['salon_logo']
            if salon_logo.filename != '':
                filename = secure_filename(salon_logo.filename)
                salon_logo.save(os.path.join(current_app.config['UPLOAD_FOLDER'] , filename))

        # Update the salon data in MongoDB
        mongo.db.salons.update_one({'_id': ObjectId(id)}, {'$set': {
            'owner_name': owner_name,
            'salon_name': salon_name,
            'salon_logo_filename': filename,
            'address': address,
            'phone_number': phone_number,
            'salon_description': salon_description
        }})
        # Redirect to the salon view page or any other page
        return redirect(url_for('salon.salon_view'))
    return render_template('Salon/EditSalon.html', salon=salon)


#Delete Salon
@salon_blueprint.route('/delete_salon/<string:id>', methods=['POST'])
def delete_salon(id):
    # Find the salon by id
    salon = mongo.db.salons.find_one({'_id': ObjectId(id)})
    if not salon:
        flash('Salon not found.', 'error')
        return redirect(url_for('salon.salon_view'))

    # Delete the salon from the database
    mongo.db.salons.delete_one({'_id': ObjectId(id)})
    
    flash('Salon deleted successfully.', 'success')
    return redirect(url_for('salon.salon_view'))


@salon_blueprint.route('/view_salon/<string:id>')
def view_salon(id):
    # Find the salon by id
    salon = mongo.db.salons.find_one({'_id': ObjectId(id)})
    if not salon:
        flash('Salon not found.', 'error')
        return redirect(url_for('salon.salon_view'))

    return render_template('Salon/ViewSalon.html', salon=salon)
