from .olap_models import (
    BasicData, ClusterAggregations, BlockAggregations,
    DistrictAggregations, AssemblyAggregations, ParliamentAggregations,
    PincodeAggregations
)
from rest_framework import serializers


class GeoJSONSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        geom = getattr(obj, self.Meta.geometry_field) if hasattr(obj, self.Meta.geometry_field) else None
        return {
            'id': getattr(obj, self.Meta.pk_field),
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': geom.coords if geom else []
            },
            'properties': {
                key: getattr(obj, key)
                for key in self.Meta.fields if key != self.Meta.geometry_field
            }
        }


class SchoolSerializer(GeoJSONSerializer):
    class Meta:
        model = BasicData
        geometry_field = 'centroid'
        pk_field = 'school_code'
        fields = [
            'school_code', 'school_name', 'cluster_name', 'centroid',
            'block_name', 'district', 'pincode', 'yeur_estd',
            'total_boys', 'total_girls', 'male_tch', 'female_tch',
            'medium_of_instruction', 'sch_management', 'sch_category',
            'library_yn', 'books_in_library', 'no_of_computers',
            'electricity', 'drinking_water', 'toilet_common', 'toilet_boys',
            'toilet_girls', 'tot_clrooms'
        ]


class ClusterSerializer(GeoJSONSerializer):
    class Meta:
        model = ClusterAggregations
        geometry_field = 'centroid'
        pk_field = 'cluster_name'
        fields = ClusterAggregations._meta.get_all_field_names()


class BlockSerializer(GeoJSONSerializer):
    class Meta:
        model = BlockAggregations
        geometry_field = 'centroid'
        pk_field = 'block_name'
        fields = BlockAggregations._meta.get_all_field_names()


class DistrictSerializer(GeoJSONSerializer):
    class Meta:
        model = DistrictAggregations
        geometry_field = 'centroid'
        pk_field = 'district_name'
        fields = DistrictAggregations._meta.get_all_field_names()


class AssemblySerializer(GeoJSONSerializer):
    class Meta:
        model = AssemblyAggregations
        geometry_field = 'centroid'
        pk_field = 'assembly_name'
        fields = AssemblyAggregations._meta.get_all_field_names()


class ParliamentSerializer(GeoJSONSerializer):
    class Meta:
        model = ParliamentAggregations
        geometry_field = 'centroid'
        pk_field = 'parliament_name'
        fields = ParliamentAggregations._meta.get_all_field_names()


class PincodeSerializer(GeoJSONSerializer):
    class Meta:
        model = PincodeAggregations
        geometry_field = 'centroid'
        pk_field = 'pincode'
        fields = PincodeAggregations._meta.get_all_field_names()
