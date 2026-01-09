document.addEventListener('DOMContentLoaded', () => {
    // --- Theme Toggle Logic ---
    const themeBtn = document.getElementById('theme-toggle');
    const iconSpan = themeBtn.querySelector('.icon');
    
    // Check local storage or system preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        iconSpan.textContent = '☀️'; // Sun icon for light mode
    }

    themeBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        if (currentTheme === 'light') {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'dark');
            iconSpan.textContent = '🌙'; // Moon icon for dark mode
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            iconSpan.textContent = '☀️';
        }
    });

    // --- DOM Elements ---
    const btnDetailed = document.getElementById('btn-detailed');
    const btnQuick = document.getElementById('btn-quick');
    const formOverlay = document.getElementById('form-overlay');
    const backBtn = document.getElementById('back-to-chat');
    const photoInput = document.getElementById('photo-input');
    const photoPreview = document.getElementById('photo-preview');
    const photoDropzone = document.getElementById('photo-dropzone');
    const resumeForm = document.getElementById('resume-form');
    const messagesContainer = document.getElementById('messages');

    // --- Dynamic List Containers ---
    const lists = {
        skill: document.getElementById('skills-list'),
        exp: document.getElementById('experience-list'),
        proj: document.getElementById('projects-list'),
        edu: document.getElementById('education-list'),
        cert: document.getElementById('certificates-list')
    };

    // --- HTML Templates ---
    const createSkillRow = () => `
        <div class="dynamic-row skill-entry">
            <button type="button" class="remove-btn" onclick="removeRow(this)">&times;</button>
            <div class="input-grid">
                <div class="field">
                    <label>Skill Category</label>
                    <input type="text" class="s-type trigger-new-row" data-type="skill" placeholder="e.g. Programming">
                </div>
                <div class="field">
                    <label>Skills (Comma separated)</label>
                    <input type="text" class="s-list" placeholder="Java, Python, C++">
                </div>
            </div>
        </div>`;

    const createExpRow = () => `
        <div class="dynamic-row exp-entry">
            <button type="button" class="remove-btn" onclick="removeRow(this)">&times;</button>
            <div class="input-grid">
                <div class="field">
                    <label>Company</label>
                    <input type="text" class="e-company trigger-new-row" data-type="exp" placeholder="Company Name">
                </div>
                <div class="field">
                    <label>Role</label>
                    <input type="text" class="e-role" placeholder="Job Title">
                </div>
            </div>
            <div class="field">
                <label>Description</label>
                <textarea class="e-desc" rows="2" placeholder="Key responsibilities..."></textarea>
            </div>
        </div>`;

    const createProjRow = () => `
        <div class="dynamic-row proj-entry">
            <button type="button" class="remove-btn" onclick="removeRow(this)">&times;</button>
            <div class="field">
                <label>Project Name</label>
                <input type="text" class="p-name trigger-new-row" data-type="proj" placeholder="Project Title">
            </div>
            <div class="field">
                <label>Description / Tech Stack</label>
                <textarea class="p-desc" rows="2" placeholder="Brief description..."></textarea>
            </div>
        </div>`;

    const createEduRow = () => `
        <div class="dynamic-row edu-entry">
            <button type="button" class="remove-btn" onclick="removeRow(this)">&times;</button>
            <div class="input-grid">
                <div class="field">
                    <label>Institution</label>
                    <input type="text" class="ed-inst trigger-new-row" data-type="edu" placeholder="University Name">
                </div>
                <div class="field">
                    <label>Degree</label>
                    <input type="text" class="ed-deg" placeholder="Degree / Certificate">
                </div>
            </div>
        </div>`;

    const createCertRow = () => `
        <div class="dynamic-row cert-entry">
            <button type="button" class="remove-btn" onclick="removeRow(this)">&times;</button>
            <div class="field">
                <label>Certificate Name</label>
                <input type="text" class="c-name trigger-new-row" data-type="cert" placeholder="Certificate Name">
            </div>
        </div>`;

    // --- Helper Functions ---
    function addRow(type) {
        let html = '';
        if (type === 'skill') html = createSkillRow();
        if (type === 'exp') html = createExpRow();
        if (type === 'proj') html = createProjRow();
        if (type === 'edu') html = createEduRow();
        if (type === 'cert') html = createCertRow();
        
        const container = lists[type];
        if (container) {
            const div = document.createElement('div');
            div.innerHTML = html;
            while (div.firstChild) {
                container.appendChild(div.firstChild);
            }
        }
    }

    window.removeRow = (btn) => {
        const row = btn.closest('.dynamic-row');
        if (row) {
            row.style.opacity = '0';
            row.style.transform = 'translateX(20px)';
            setTimeout(() => row.remove(), 300);
        }
    };

    // --- Event Listeners ---
    document.getElementById('add-skill-btn').addEventListener('click', () => addRow('skill'));
    document.getElementById('add-exp-btn').addEventListener('click', () => addRow('exp'));
    document.getElementById('add-proj-btn').addEventListener('click', () => addRow('proj'));
    document.getElementById('add-edu-btn').addEventListener('click', () => addRow('edu'));
    document.getElementById('add-cert-btn').addEventListener('click', () => addRow('cert'));

    document.addEventListener('input', (e) => {
        if (e.target.classList.contains('trigger-new-row')) {
            if (e.target.value.includes(',')) {
                e.target.value = e.target.value.replace(',', ''); 
                const type = e.target.dataset.type;
                addRow(type);
                const container = lists[type];
                const newRow = container.lastElementChild;
                if (newRow) {
                    const input = newRow.querySelector('.trigger-new-row');
                    if (input) input.focus();
                }
            }
        }
    });

    // --- Photo Upload Logic ---
    photoDropzone.addEventListener('click', () => photoInput.click());
    
    photoInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                photoPreview.innerHTML = `<img src="${e.target.result}" alt="Preview" style="width:100%; height:100%; object-fit:cover;">`;
                photoDropzone.style.borderStyle = 'solid';
                photoDropzone.style.borderColor = 'var(--accent)';
            };
            reader.readAsDataURL(file);
        }
    });

    // --- Navigation Logic ---
    const toggleForm = (show) => {
        if (show) {
            formOverlay.classList.remove('hidden');
            document.getElementById('detailed-fields').classList.remove('hidden');
            document.getElementById('quick-fields').classList.add('hidden');
            
            Object.keys(lists).forEach(key => {
                if (lists[key] && lists[key].children.length === 0) {
                    addRow(key);
                }
            });
        } else {
            formOverlay.classList.add('hidden');
        }
    };

    const toggleQuick = () => {
        formOverlay.classList.remove('hidden');
        document.getElementById('quick-fields').classList.remove('hidden');
        document.getElementById('detailed-fields').classList.add('hidden');
    };

    btnDetailed.addEventListener('click', () => toggleForm(true));
    btnQuick.addEventListener('click', toggleQuick);
    backBtn.addEventListener('click', () => formOverlay.classList.add('hidden'));

    // --- JSON Generation ---
    resumeForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const output = {
            personal_info: {
                full_name: document.getElementById('full_name').value,
                phone_number: document.getElementById('phone_number').value,
                email: document.getElementById('email').value
            },
            objective: document.getElementById('objective').value,
            skills: [],
            experience: [],
            projects: [],
            education: [],
            certificates: []
        };

        document.querySelectorAll('.skill-entry').forEach(row => {
            const type = row.querySelector('.s-type').value;
            const listStr = row.querySelector('.s-list').value;
            if (type) {
                output.skills.push({
                    skill_type: type,
                    skills: listStr ? listStr.split(',').map(s => s.trim()).filter(s => s) : []
                });
            }
        });

        document.querySelectorAll('.exp-entry').forEach(row => {
            const comp = row.querySelector('.e-company').value;
            if (comp) {
                output.experience.push({
                    company: comp,
                    role: row.querySelector('.e-role').value,
                    description: row.querySelector('.e-desc').value
                });
            }
        });

        document.querySelectorAll('.proj-entry').forEach(row => {
            const name = row.querySelector('.p-name').value;
            if (name) {
                output.projects.push({
                    name: name,
                    description: row.querySelector('.p-desc').value
                });
            }
        });

        document.querySelectorAll('.edu-entry').forEach(row => {
            const inst = row.querySelector('.ed-inst').value;
            if (inst) {
                output.education.push({
                    institution: inst,
                    degree: row.querySelector('.ed-deg').value
                });
            }
        });

        document.querySelectorAll('.cert-entry').forEach(row => {
            const name = row.querySelector('.c-name').value;
            if (name) output.certificates.push(name);
        });

        console.log("FINAL JSON OUTPUT:", output);
        
        formOverlay.classList.add('hidden');
        const botMsg = document.createElement('div');
        botMsg.className = 'message bot';
        botMsg.innerHTML = `
            <div class="avatar">AI</div>
            <div class="bubble" style="border-color: var(--success);">
                <p>✅ <b>JSON Generated Successfully!</b></p>
                <p class="secondary">Check the browser console (F12) to view the schema-compliant object.</p>
            </div>`;
        messagesContainer.appendChild(botMsg);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    });
});