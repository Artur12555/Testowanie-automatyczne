import java.util.ArrayList;
import java.util.List;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@Path("/books")
public class BookAPI {
    
    // Mocked data for /books endpoint
    private static List<Book> books = new ArrayList<Book>();
    static {
        books.add(new Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"));
        books.add(new Book(2, "To Kill a Mockingbird", "Harper Lee", "9780446310789"));
        books.add(new Book(3, "1984", "George Orwell", "9780451524935"));
    }
    
    // /books endpoint
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<Book> getBooks() {
        return books;
    }
    
    // /books/:id endpoint
    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response getBook(@PathParam("id") int id) {
        for (Book book : books) {
            if (book.getId() == id) {
                return Response.ok(book, MediaType.APPLICATION_JSON).build();
            }
        }
        return Response.status(Response.Status.NOT_FOUND).build();
    }
    
    // /books endpoint with query parameter
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response createBook(Book book) {
        if (book == null || book.getTitle() == null || book.getAuthor() == null || book.getIsbn() == null) {
            return Response.status(Response.Status.BAD_REQUEST).build();
        }
        book.setId(books.size() + 1);
        books.add(book);
        return Response.ok(book, MediaType.APPLICATION_JSON).build();
    }
    
    // Book data model
    public static class Book {
        private int id;
        private String title;
        private String author;
        private String isbn;
        
        public Book() {}
        
        public Book(int id, String title, String author, String isbn) {
            this.id = id;
            this.title = title;
            this.author = author;
            this.isbn = isbn;
        }
        
        public int getId() {
            return id;
        }
        
        public void setId(int id) {
            this.id = id;
        }
        
        public String getTitle() {
            return title;
        }
        
        public void setTitle(String title) {
            this.title = title;
        }
        
        public String getAuthor() {
            return author;
        }
        
        public void setAuthor(String author) {
            this.author = author;
        }
        
        public String getIsbn() {
            return isbn;
        }
        
        public void setIsbn(String isbn) {
            this.isbn = isbn;
        }
    }
}