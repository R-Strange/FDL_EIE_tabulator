from dataclasses import dataclass


@dataclass
class MetadataDataclass:
    uuid: str
    feature_type: str
    subtype: str
    wkt_latlong: str
    wkt_xy: str
    image_filename: str