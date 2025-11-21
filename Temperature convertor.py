import math
import sys
from datetime import datetime

class TemperatureConverter:
    def __init__(self):
        self.conversion_history = []
        self.common_temperatures = {
            'Absolute Zero': {'C': -273.15, 'F': -459.67, 'K': 0},
            'Freezing Point of Water': {'C': 0, 'F': 32, 'K': 273.15},
            'Room Temperature': {'C': 20, 'F': 68, 'K': 293.15},
            'Human Body Temperature': {'C': 37, 'F': 98.6, 'K': 310.15},
            'Boiling Point of Water': {'C': 100, 'F': 212, 'K': 373.15}
        }
    
    def celsius_to_fahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit"""
        fahrenheit = (celsius * 9/5) + 32
        return round(fahrenheit, 2)
    
    def fahrenheit_to_celsius(self, fahrenheit):
        """Convert Fahrenheit to Celsius"""
        celsius = (fahrenheit - 32) * 5/9
        return round(celsius, 2)
    
    def celsius_to_kelvin(self, celsius):
        """Convert Celsius to Kelvin"""
        kelvin = celsius + 273.15
        return round(kelvin, 2)
    
    def kelvin_to_celsius(self, kelvin):
        """Convert Kelvin to Celsius"""
        celsius = kelvin - 273.15
        return round(celsius, 2)
    
    def fahrenheit_to_kelvin(self, fahrenheit):
        """Convert Fahrenheit to Kelvin"""
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        kelvin = self.celsius_to_kelvin(celsius)
        return round(kelvin, 2)
    
    def kelvin_to_fahrenheit(self, kelvin):
        """Convert Kelvin to Fahrenheit"""
        celsius = self.kelvin_to_celsius(kelvin)
        fahrenheit = self.celsius_to_fahrenheit(celsius)
        return round(fahrenheit, 2)
    
    def log_conversion(self, value, from_unit, to_unit, result):
        """Log conversion to history"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            'timestamp': timestamp,
            'input': f"{value}°{from_unit}",
            'output': f"{result}°{to_unit}",
            'conversion': f"{from_unit} → {to_unit}"
        }
        self.conversion_history.append(entry)
    
    def convert_temperature(self, value, from_unit, to_unit):
        """Main conversion function"""
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        # Validate input
        if from_unit not in ['C', 'F', 'K'] or to_unit not in ['C', 'F', 'K']:
            raise ValueError("Invalid temperature unit. Use C, F, or K.")
        
        if from_unit == to_unit:
            return value
        
        # Perform conversion
        if from_unit == 'C' and to_unit == 'F':
            result = self.celsius_to_fahrenheit(value)
        elif from_unit == 'C' and to_unit == 'K':
            result = self.celsius_to_kelvin(value)
        elif from_unit == 'F' and to_unit == 'C':
            result = self.fahrenheit_to_celsius(value)
        elif from_unit == 'F' and to_unit == 'K':
            result = self.fahrenheit_to_kelvin(value)
        elif from_unit == 'K' and to_unit == 'C':
            result = self.kelvin_to_celsius(value)
        elif from_unit == 'K' and to_unit == 'F':
            result = self.kelvin_to_fahrenheit(value)
        
        # Log the conversion
        self.log_conversion(value, from_unit, to_unit, result)
        return result
    
    def show_conversion_history(self):
        """Display conversion history"""
        if not self.conversion_history:
            print("\nNo conversions recorded yet.")
            return
        
        print("\n" + "="*60)
        print("CONVERSION HISTORY")
        print("="*60)
        for i, entry in enumerate(self.conversion_history[-10:], 1):  # Show last 10
            print(f"{i}. {entry['timestamp']}")
            print(f"   {entry['input']} → {entry['output']} ({entry['conversion']})")
            print()
    
    def clear_history(self):
        """Clear conversion history"""
        self.conversion_history.clear()
        print("Conversion history cleared!")
    
    def show_common_temperatures(self):
        """Display common temperature references"""
        print("\n" + "="*70)
        print("COMMON TEMPERATURE REFERENCES")
        print("="*70)
        print(f"{'Description':<25} {'Celsius':<10} {'Fahrenheit':<12} {'Kelvin':<10}")
        print("-"*70)
        
        for desc, temps in self.common_temperatures.items():
            print(f"{desc:<25} {temps['C']:<10} {temps['F']:<12} {temps['K']:<10}")
    
    def temperature_analysis(self, value, unit):
        """Provide analysis of a temperature"""
        unit = unit.upper()
        
        # Convert to all units for analysis
        if unit == 'C':
            c = value
            f = self.celsius_to_fahrenheit(value)
            k = self.celsius_to_kelvin(value)
        elif unit == 'F':
            c = self.fahrenheit_to_celsius(value)
            f = value
            k = self.fahrenheit_to_kelvin(value)
        elif unit == 'K':
            c = self.kelvin_to_celsius(value)
            f = self.kelvin_to_fahrenheit(value)
            k = value
        
        print(f"\n📊 Temperature Analysis for {value}°{unit}:")
        print(f"   Celsius: {c}°C")
        print(f"   Fahrenheit: {f}°F")
        print(f"   Kelvin: {k}°K")
        
        # Provide context
        print("\n🌡️  Context:")
        if c < -273.15:
            print("   ❄️  Below absolute zero (theoretically impossible)")
        elif c == -273.15:
            print("   ❄️  Absolute zero - coldest possible temperature")
        elif c < 0:
            print("   ❄️  Below freezing point of water")
        elif c == 0:
            print("   💧 Freezing point of water")
        elif 0 < c < 20:
            print("   🏔️  Cold weather")
        elif 20 <= c <= 25:
            print("   😊 Comfortable room temperature")
        elif c == 37:
            print("   👤 Normal human body temperature")
        elif 37 < c < 100:
            print("   🔥 Hot")
        elif c == 100:
            print("   💨 Boiling point of water")
        else:
            print("   🔥 Very hot!")

def interactive_mode():
    """Interactive mode with menu"""
    converter = TemperatureConverter()
    
    while True:
        print("\n" + "="*50)
        print("        TEMPERATURE CONVERTER")
        print("="*50)
        print("1. Convert Temperature")
        print("2. Common Temperature References")
        print("3. Temperature Analysis")
        print("4. Conversion History")
        print("5. Clear History")
        print("6. Help")
        print("0. Exit")
        print("-"*50)
        
        try:
            choice = input("Enter your choice (0-6): ").strip()
            
            if choice == '0':
                print("Goodbye! 👋")
                break
            
            elif choice == '1':
                print("\n🎯 Convert Temperature")
                print("Available units: C (Celsius), F (Fahrenheit), K (Kelvin)")
                
                value = float(input("Enter temperature value: "))
                from_unit = input("Enter from unit (C/F/K): ").strip().upper()
                to_unit = input("Enter to unit (C/F/K): ").strip().upper()
                
                result = converter.convert_temperature(value, from_unit, to_unit)
                print(f"\n✅ {value}°{from_unit} = {result}°{to_unit}")
            
            elif choice == '2':
                converter.show_common_temperatures()
            
            elif choice == '3':
                print("\n📊 Temperature Analysis")
                value = float(input("Enter temperature value: "))
                unit = input("Enter unit (C/F/K): ").strip().upper()
                converter.temperature_analysis(value, unit)
            
            elif choice == '4':
                converter.show_conversion_history()
            
            elif choice == '5':
                converter.clear_history()
            
            elif choice == '6':
                show_help()
            
            else:
                print("❌ Invalid choice! Please try again.")
        
        except ValueError as e:
            print(f"❌ Input error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")

def command_line_mode():
    """Command-line interface for quick conversions"""
    converter = TemperatureConverter()
    
    if len(sys.argv) < 4:
        print("Usage: python temp_converter.py <value> <from_unit> <to_unit>")
        print("Example: python temp_converter.py 100 C F")
        print("Units: C (Celsius), F (Fahrenheit), K (Kelvin)")
        return
    
    try:
        value = float(sys.argv[1])
        from_unit = sys.argv[2].upper()
        to_unit = sys.argv[3].upper()
        
        result = converter.convert_temperature(value, from_unit, to_unit)
        print(f"{value}°{from_unit} = {result}°{to_unit}")
        
    except Exception as e:
        print(f"Error: {e}")

def show_help():
    """Display help information"""
    print("""
🌡️ TEMPERATURE CONVERTER HELP
─────────────────────────────

CONVERSION FORMULAS:
• Celsius to Fahrenheit: (°C × 9/5) + 32
• Fahrenheit to Celsius: (°F - 32) × 5/9
• Celsius to Kelvin: °C + 273.15
• Kelvin to Celsius: K - 273.15

ABSOLUTE ZERO:
• Celsius: -273.15°C
• Fahrenheit: -459.67°F
• Kelvin: 0K

COMMON TEMPERATURES:
• Water freezes: 0°C, 32°F, 273.15K
• Human body: 37°C, 98.6°F, 310.15K
• Water boils: 100°C, 212°F, 373.15K

USAGE:
Interactive Mode: Run without arguments
Command Line: python temp_converter.py <value> <from> <to>
Example: python temp_converter.py 25 C F
""")

def quick_conversion_tool():
    """Simple quick conversion tool"""
    converter = TemperatureConverter()
    
    print("🚀 Quick Temperature Converter")
    print("Enter temperatures like: '25 C to F' or '100c f'")
    print("Type 'quit' to exit, 'help' for help")
    
    while True:
        try:
            user_input = input("\n➡️  Enter conversion: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            elif user_input.lower() in ['help', 'h']:
                show_help()
                continue
            elif user_input.lower() in ['common', 'references']:
                converter.show_common_temperatures()
                continue
            
            # Parse input like "25 C to F" or "100c f"
            parts = user_input.split()
            if len(parts) >= 3:
                # Extract value and units
                value = float(parts[0])
                from_unit = parts[1].upper().replace('°', '').replace('º', '')
                to_unit = parts[-1].upper().replace('°', '').replace('º', '')
                
                # Handle cases where units might be attached to numbers
                if not from_unit.isalpha():
                    # Try to extract unit from the number
                    for char in parts[1]:
                        if char.isalpha():
                            from_unit = char.upper()
                            break
                
                if not to_unit.isalpha():
                    for char in parts[-1]:
                        if char.isalpha():
                            to_unit = char.upper()
                            break
                
                # Convert single letters to units
                unit_map = {'C': 'C', 'F': 'F', 'K': 'K'}
                from_unit = unit_map.get(from_unit, from_unit)
                to_unit = unit_map.get(to_unit, to_unit)
                
                result = converter.convert_temperature(value, from_unit, to_unit)
                print(f"✅ {value}°{from_unit} = {result}°{to_unit}")
                
                # Show quick analysis for interesting temperatures
                if from_unit == 'C' and (value == 0 or value == 100 or value == 37 or value == -273.15):
                    print("💡 Interesting fact above!")
            
            else:
                print("❌ Invalid format. Use: '25 C to F' or '100c f'")
        
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main function to choose mode"""
    print("🌡️  Temperature Converter")
    print("=" * 30)
    
    if len(sys.argv) > 1:
        # Command line mode
        command_line_mode()
    else:
        # Interactive mode selection
        print("Choose mode:")
        print("1. Interactive Menu Mode")
        print("2. Quick Conversion Tool")
        print("3. Command Line Help")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            interactive_mode()
        elif choice == '2':
            quick_conversion_tool()
        elif choice == '3':
            show_help()
        else:
            print("Starting Interactive Mode...")
            interactive_mode()

# Example usage functions
def conversion_examples():
    """Show example conversions"""
    converter = TemperatureConverter()
    
    examples = [
        (0, 'C', 'F'),      # Freezing point
        (100, 'C', 'F'),    # Boiling point
        (32, 'F', 'C'),     # Freezing point
        (212, 'F', 'C'),    # Boiling point
        (0, 'C', 'K'),      # Freezing to Kelvin
        (-273.15, 'C', 'K') # Absolute zero
    ]
    
    print("\n📚 Conversion Examples:")
    print("-" * 40)
    for value, from_unit, to_unit in examples:
        result = converter.convert_temperature(value, from_unit, to_unit)
        print(f"{value}°{from_unit} = {result}°{to_unit}")

if __name__ == "__main__":
    # Run examples if requested
    if '--examples' in sys.argv:
        conversion_examples()
    else:
        main()