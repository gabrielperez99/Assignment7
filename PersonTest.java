package assignment7;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PersonTest {
    @Test
    public void testGetName() {
        Person person = new Person("John Doe", 25);
        String name = person.getName();
        assertEquals("John Doe", name);
    }

    @Test
    public void testGetAge() {
        Person person = new Person("Jane Smith", 30);
        int age = person.getAge();
        assertEquals(30, age);
    }

    @Test
    public void testIsAdult() {
        Person adult = new Person("John Doe", 25);
        Person child = new Person("Jane Smith", 12);
        assertTrue(adult.isAdult());
        assertFalse(child.isAdult());
    }
}
