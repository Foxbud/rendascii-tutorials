import math
import os.path

from rendascii.interface import Engine as REngine


# Directories.
ROOT_DIR = os.path.dirname(__file__)
ASSET_DIR = os.path.join(ROOT_DIR, 'assets')
COLORMAP_DIR = os.path.join(ASSET_DIR, 'colormaps')
MODEL_DIR = os.path.join(ASSET_DIR, 'models')
MATERIAL_DIR = os.path.join(ASSET_DIR, 'materials')


def main():
	# Initialize the rendering engine.
	re = REngine(
		colormap_dir=COLORMAP_DIR,
		model_dir=MODEL_DIR,
		material_dir=MATERIAL_DIR,
		num_workers=0
	)

	# Import assets.
	re.load_colormap(
		colormap_name='object',
		colormap_filename='object.json'
	)
	re.load_model(
		model_name='tetra',
		model_filename='tetrahedron.obj',
		right_handed=True
	)

	# Create render instances.
	cam = re.create_camera(
		resolution=(50, 25),
		near=0.001,
		far=11.0,
		fov=math.radians(80.0),
		ratio=1.5,
		fog_char=' ',
		culling=False
	)
	tetra = re.create_model_instance(
		model_name='tetra',
		colormap_name='object'
	)

	# Transform render instances.
	tetra.set_transformation(
		(
			(1.0, 0.0, 0.0, 0.0),
			(0.0, 1.0, 0.0, 0.0),
			(0.0, 0.0, 1.0, 1.25),
			(0.0, 0.0, 0.0, 1.0),
		)
	)

	# Render frame!
	frame = re.render_frame(
		camera=cam,
		as_str=True
	)
	print(frame)


if __name__ == '__main__':
	main()
