from flask import Flask, jsonify, url_for, request
import requests
import os

app = Flask(__name__)

# Example function to fetch data from an external API
def fetch_external_data():
    url = "https://api.factorialhr.com/api/v2/core/employees"
    headers = {

            'Content-Type': 'application/json',
    'x-api-key': '9a2ea13f8509870f756a759e6c58a281e010c037ae757640781c4759be160dba',
    'Accept': '*/*'

    }
    response = requests.get(url, headers=headers)
    return response.json()

# Example function to convert data to OData format
def convert_to_odata(data):
    # Simplified conversion logic
    odata = {
        '@odata.context': request.url_root + 'odata/$metadata',
        'value': data
    }
    return odata

@app.route('/odata', methods=['GET'])
def odata_service():
    external_data = fetch_external_data()
    odata_formatted_data = convert_to_odata(external_data)
    return jsonify(odata_formatted_data)

@app.route('/odata/$metadata', methods=['GET'])
def odata_metadata():
    metadata = """<?xml version="1.0" encoding="utf-8"?>
    <edmx:Edmx Version="4.0" xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx">
      <edmx:DataServices>
        <Schema Namespace="MyService" xmlns="http://docs.oasis-open.org/odata/ns/edm">
          <EntityType Name="Person">
            <Key>
              <PropertyRef Name="id"/>
            </Key>
            <Property Name="address_line_1" Type="Edm.String" Nullable="true"/>
            <Property Name="address_line_2" Type="Edm.String" Nullable="true"/>
            <Property Name="bank_number" Type="Edm.String" Nullable="true"/>
            <Property Name="bank_number_format" Type="Edm.String" Nullable="true"/>
            <Property Name="birthday_on" Type="Edm.DateTimeOffset" Nullable="true"/>
            <Property Name="city" Type="Edm.String" Nullable="true"/>
            <Property Name="company_id" Type="Edm.Int32" Nullable="false"/>
            <Property Name="company_identifier" Type="Edm.String" Nullable="true"/>
            <Property Name="contact_name" Type="Edm.String" Nullable="true"/>
            <Property Name="contact_number" Type="Edm.String" Nullable="true"/>
            <Property Name="country" Type="Edm.String" Nullable="true"/>
            <Property Name="created_at" Type="Edm.DateTimeOffset" Nullable="false"/>
            <Property Name="email" Type="Edm.String" Nullable="false"/>
            <Property Name="first_name" Type="Edm.String" Nullable="false"/>
            <Property Name="full_name" Type="Edm.String" Nullable="false"/>
            <Property Name="gender" Type="Edm.String" Nullable="true"/>
            <Property Name="id" Type="Edm.Int32" Nullable="false"/>
            <Property Name="identifier" Type="Edm.String" Nullable="true"/>
            <Property Name="identifier_type" Type="Edm.String" Nullable="true"/>
            <Property Name="last_name" Type="Edm.String" Nullable="false"/>
            <Property Name="legal_entity_id" Type="Edm.Int32" Nullable="false"/>
            <Property Name="location_id" Type="Edm.Int32" Nullable="false"/>
            <Property Name="login_email" Type="Edm.String" Nullable="false"/>
            <Property Name="manager_id" Type="Edm.Int32" Nullable="true"/>
            <Property Name="nationality" Type="Edm.String" Nullable="true"/>
            <Property Name="phone_number" Type="Edm.String" Nullable="true"/>
            <Property Name="postal_code" Type="Edm.String" Nullable="true"/>
            <Property Name="preferred_name" Type="Edm.String" Nullable="true"/>
            <Property Name="social_security_number" Type="Edm.String" Nullable="true"/>
            <Property Name="state" Type="Edm.String" Nullable="true"/>
            <Property Name="swift_bic" Type="Edm.String" Nullable="true"/>
            <Property Name="tax_id" Type="Edm.String" Nullable="true"/>
            <Property Name="team_ids" Type="Collection(Edm.Int32)" Nullable="true"/>
            <Property Name="terminated_on" Type="Edm.DateTimeOffset" Nullable="true"/>
            <Property Name="termination_observations" Type="Edm.String" Nullable="true"/>
            <Property Name="termination_reason" Type="Edm.String" Nullable="true"/>
            <Property Name="termination_reason_type" Type="Edm.String" Nullable="true"/>
            <Property Name="termination_type_description" Type="Edm.String" Nullable="true"/>
            <Property Name="timeoff_manager_id" Type="Edm.Int32" Nullable="true"/>
            <Property Name="timeoff_policy_id" Type="Edm.Int32" Nullable="false"/>
            <Property Name="updated_at" Type="Edm.DateTimeOffset" Nullable="false"/>
          </EntityType>
        </Schema>
      </edmx:DataServices>
    </edmx:Edmx>
    """
    return metadata, 200, {'Content-Type': 'application/xml'}


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Set debug to False for production
    app.run(host='0.0.0.0', port=port, debug=False)
