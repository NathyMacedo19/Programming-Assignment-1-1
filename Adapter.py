class OldPhysicsSystem:
    """Existing game physics system"""
    def move_object(self, x, y):
        print(f"Moving object to ({x}, {y})")

    def check_collision(self, obj1, obj2):
        print(f"Checking collision between {obj1} and {obj2}")

class NewPhysicsEngine:
    """New physics engine with a different API"""
    def set_position(self, x, y):
        print(f"New Physics Engine: Setting position to ({x}, {y})")

    def detect_collision(self, obj1, obj2):
        print(f"New Physics Engine: Collision detected between {obj1} and {obj2}")        

class PhysicsAdapter:
    """Adapter to make the new physics engine compatible with the existing game system"""
    def __init__(self, new_engine):
        self.new_engine = new_engine  # Reference to the new physics engine

    def move_object(self, x, y):
        """Translate move_object to set_position"""
        self.new_engine.set_position(x, y)

    def check_collision(self, obj1, obj2):
        """Translate check_collision to detect_collision"""
        self.new_engine.detect_collision(obj1, obj2)

# Use the new physics engine with the adapter
new_engine = NewPhysicsEngine()
physics_system = PhysicsAdapter(new_engine)  # Using the adapter

# Game logic remains unchanged, but it now works with the new engine
physics_system.move_object(10, 20)
physics_system.check_collision("Player", "Enemy")        