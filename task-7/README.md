
# Cherry-Picking a Commit in Git

## Objective
This guide demonstrates how to selectively apply a commit from one branch (`features`) to another (`main`) using `git cherry-pick`.

---

## Initial Setup

### **Before Cherry-Pick (Main Branch)**
The `main` branch has the following HTML structure:

```html
<html>
<body>
    <h1>Welcome</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta, veritatis!</p>
</body>
</html>

```

### **Before Cherry-Pick (Features Branch)**

The `features` branch includes additional elements: a navigation bar and a footer.

```html
<html>
<body>
    <nav>
        Nav Bar
    </nav>
    <h1>Welcome</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta, veritatis!</p>
    <footer>
        Footer of the website
    </footer>
</body>
</html>

```

----------

## **Commit History in `features`**

Run the command below to view the commit history:

```bash
git log --oneline --graph --all

```

Example output:

```
4ce5b4b (HEAD -> features) added footer
8277fd8 added navbar

```

-   `8277fd8` → Commit that adds the **Nav Bar**
-   `4ce5b4b` → Commit that adds the **Footer**

----------

## **Cherry-Picking a Commit**

To apply only the **Nav Bar** commit (`8277fd8`) to `main`:

```bash
git checkout main
git cherry-pick 8277fd8

```

After this, the `main` branch now looks like:

```html
<html>
<body>
    <nav>
        Nav Bar
    </nav>
    <h1>Welcome</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta, veritatis!</p>
</body>
</html>

```

The **Footer** is not included because it was added in a separate commit (`4ce5b4b`).

----------

## **Verifying the Commit**

To confirm that only the Nav Bar was applied, check the commit history in `main`:

```bash
git log --oneline

```

You should see an entry for the cherry-picked commit.

----------

## **Conclusion**

-   Cherry-picking allows selective application of commits from one branch to another.
-   Only the specified commit (`8277fd8`) was applied, so the footer (`4ce5b4b`) is missing.

